# Demo Docker Image

Every published release (release candidates included) gets a ready-to-run demo image: the shop, installed with demo data, plus its database in one container. It's the quickest way to try O3-Shop: one command, no web server, PHP or database setup.

```{warning}
**For demos only, not for production.** The database runs inside the container and starts from the original demo state every time a new container is created.
```

## Start the demo

```bash
docker run -p 8080:80 ghcr.io/o3-shop/o3-shop-demo:v1.7.2
```

- Shop: <http://localhost:8080>
- Admin: <http://localhost:8080/admin/> (`admin@example.com` / `admin123`)

Replace `v1.7.2` with the release you want to try. Release candidates have their own tags (e.g. `v1.7.3-RC1`), and `latest` follows the newest final release. All tags are listed in the <a target="_blank" href="https://github.com/orgs/o3-shop/packages/container/package/o3-shop-demo">package registry</a>. Images exist from the first release that contains the demo image (v1.7.2-RC2).

## Settings

| Variable | Default | Purpose |
|---|---|---|
| `O3_SHOP_URL` | `http://localhost:8080` | URL the shop is reached under. Set it when you use another port or host, e.g. `docker run -p 9000:80 -e O3_SHOP_URL=http://localhost:9000 …` |
| `O3_ADMIN_EMAIL` | `admin@example.com` | Admin login |
| `O3_ADMIN_PASSWORD` | `admin123` | Admin password. Set your own for anything reachable by others. |
| `O3_HTTPS` | `letsencrypt` | HTTPS only: `letsencrypt` = the container terminates TLS with a Let's Encrypt certificate; `proxy` = a reverse proxy in front terminates TLS. See [HTTPS](#https) below. |
| `O3_ACME_EMAIL` | (none) | `letsencrypt` only: contact address for the certificate |
| `O3_ACME_STAGING` | `0` | `letsencrypt` only: `1` uses the Let's Encrypt staging CA (untrusted certificates, for testing without rate limits) |

## Run under another URL

The shop builds its links from `O3_SHOP_URL`. If you open it under any address other than `http://localhost:8080` (another port, the machine's IP address or a host name), set the variable to exactly that address. Otherwise links point to the wrong place.

```bash
docker run -p 9000:80 -e O3_SHOP_URL=http://localhost:9000 ghcr.io/o3-shop/o3-shop-demo:v1.7.2
docker run -p 80:80 -e O3_SHOP_URL=http://demo.example.com ghcr.io/o3-shop/o3-shop-demo:v1.7.2
```

The URL is applied every time the container starts. To change it, create a new container with the new value; with the named volumes from "Keep your changes" below, your data carries over. Only a plain `http(s)://` URL is accepted (letters, digits and `. : _ ~ / - [ ]`); anything else stops the container at startup with an error message.

(https)=
## HTTPS

```{note}
HTTPS needs an image from the first release after `v1.7.2`. Replace `<release-tag>` below with that release or a newer one.
```

### With a Let's Encrypt certificate

With an `https://` URL the demo serves the shop over HTTPS itself: Apache obtains a Let's Encrypt certificate for the host and renews it while the container runs. Using an https URL accepts the <a target="_blank" href="https://letsencrypt.org/repository/">Let's Encrypt Subscriber Agreement</a>.

```bash
docker run -p 80:80 -p 443:443 \
  -e O3_SHOP_URL=https://<your-host> \
  -v o3-demo-certs:/etc/apache2/md \
  ghcr.io/o3-shop/o3-shop-demo:<release-tag>
```

- **Requirements:** the host name resolves to the machine, and ports 80 and 443 are reachable from the internet as they are. Let's Encrypt checks the host over port 80; an https URL with another port stops the container at startup.
- **Redirects:** plain http requests, and https requests by IP address or another host name, are redirected to the shop's https URL.
- **First start:** until the certificate is active (usually within a minute), https requests for the host get `503 Service Unavailable`. `docker logs` shows the progress. If Let's Encrypt can't issue the certificate, a line says so, the errors before it name the cause, and Apache retries automatically.
- **Keep the certificates** in a named volume (`/etc/apache2/md`, as above). Without one, every new container requests a new certificate, and Let's Encrypt limits how many duplicate certificates a host gets per week.
- **Public host names only:** `localhost`, IP addresses, reserved names (`.test`, `.local`, `example.com` and its subdomains, …) and names without a dot stop the container at startup. For local tests, use an http URL.
- **Testing:** `O3_ACME_STAGING=1` uses the Let's Encrypt staging CA. Give it a separate certificate volume, so a later production run doesn't start from the untrusted staging certificate.

### Behind a reverse proxy

If a reverse proxy (nginx, Traefik, Caddy, …) terminates TLS and forwards plain http to the container, set `O3_HTTPS=proxy`. The container then uses no certificate and doesn't redirect; the shop builds https links and treats every request as https. Any host name and port work, `localhost` included:

```bash
docker run -p 127.0.0.1:8080:80 \
  -e O3_SHOP_URL=https://shop.example.org -e O3_HTTPS=proxy \
  ghcr.io/o3-shop/o3-shop-demo:<release-tag>
```

```{warning}
Make the container reachable only by the proxy (bind the port to `127.0.0.1` as above, or use a private Docker network). The shop treats every request as https, also one that bypasses the proxy over plain http.
```

The proxy must forward the original `Host` header (nginx: `proxy_set_header Host $host;`).

## Keep your changes

Changes stay as long as you keep the container (`docker stop` / `docker start`). To keep them across new containers, use named volumes for the database and the uploaded pictures:

```bash
docker run -p 8080:80 \
  -v o3-demo-db:/var/lib/mysql \
  -v o3-demo-pictures:/var/www/html/source/out/pictures \
  ghcr.io/o3-shop/o3-shop-demo:v1.7.2
```

On first use Docker fills empty named volumes with the image's demo data. Don't use empty bind mounts (host directories) for these paths: they hide the installed data and the shop won't start. A volume created with an older image keeps that version's database, so start with fresh volumes when you switch to a newer release.

## E-mail

The demo sends no e-mail. Registration, order and newsletter mails are accepted and then discarded; `docker logs` shows one line per discarded mail with its recipient. The shop's SMTP settings stay empty even if you set them in the admin.

```{note}
The `v1.7.2-RC2` and `v1.7.2-RC3` images predate this: there, any action that sends a mail (e.g. registering with the newsletter box ticked) ends on the maintenance page. Use the current release, `v1.7.2`.
```

## Build it yourself

The image is built from the <a target="_blank" href="https://github.com/o3-shop/o3-shop/tree/b-1.7/docker/demo">`docker/demo/`</a> directory of the `o3-shop/o3-shop` repository, whose <a target="_blank" href="https://github.com/o3-shop/o3-shop#demo-docker-image">README</a> is the reference for this page:

```bash
docker build -f docker/demo/Dockerfile -t o3-shop-demo .
```
