# Modules

Extend the functionality of your O3-Shop with modules.

Use modules to

- map the business model of a shop operator
- to change the different areas of the online shop
  - the presentation of articles and categories
  - the order process
  - the payment
  - the shipping
  - offers and bonuses
- connect Enterprise Resource Planning (ERP) or content management systems with the O3-Shop
- exchange information with systems for Customer Relationship Management (CRM) and Product Information Management (PIM)

This part of the documentation describes modules for the O3-Shop.

## CAPTCHA providers

O3-Shop protects its standard frontend forms — contact, newsletter, registration,
forgot password, price alarm, suggest and invite — against automated abuse with a
CAPTCHA. The CAPTCHA layer is **pluggable**: the storefront widget and the central
**Admin → CAPTCHA** configuration screen are part of the O3-Shop core, while the actual
CAPTCHA implementation is supplied by a provider module. Providers register themselves
via the `oxid.captcha.provider` service tag, so the active protection method can be
chosen in the admin without changing the shop core, and further providers can be added
simply by installing a module.

The following providers are available. This page is only an overview — see the linked
project for each provider's installation and configuration details:

- {{ '[Simple Captcha]({}../../projects/captcha/)'.format(baseurl) }} — the built-in graphical image challenge (distorted characters).
- [Google reCAPTCHA](https://github.com/o3-shop/googlerecaptcha-module) — Google reCAPTCHA v2, v2 Invisible and v3 (score-based).
- [Altcha](https://github.com/o3-shop/altcha-module) — self-hosted, privacy-friendly proof-of-work CAPTCHA (no third-party calls, GDPR-clean).

Developers can add their own provider by implementing the core `CaptchaProviderInterface`
and registering it with the `oxid.captcha.provider` service tag.

## Further modules

- {{ '[TinyMCE editor]({}../../projects/tinymce/)'.format(baseurl) }}
