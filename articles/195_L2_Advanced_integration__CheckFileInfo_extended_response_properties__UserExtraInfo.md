---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#userextrainfo"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "userextrainfo"
title: "UserExtraInfo"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / UserExtraInfo"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / UserExtraInfo"
---
JSON object that contains additional info about the user, for example the avatar image.

Example: User’s additional info

```
{
  'avatar': 'http://url/to/user/avatar',
  'mail': 'user@server.com',
}
```

Example: User’s additional info via PHP

```
'UserExtraInfo' => [ 'avatar' => 'http://url/to/user/avatar', 'mail' => 'user@server.com' ]
```

Important

There is strict Content Security Policy that restricts image resources (`img-src`), therefore the avatar URL must not violate the CSP, otherwise it will show as broken images.

Deprecated since version 24.04.4: The `is_admin` boolean property is recommended to be set by integration. It should be `true` when the user has administrator rights in the integration, and `false` otherwise. Some functionality of Collabora Online, such as update check and server audit are supposed to be shown to administrators only. Use IsAdminUser instead for 24.04.4 and newer.

Deprecated since version 24.04.4: The `is_guest` boolean propery may be set by the integration, when the user is guest, i.e. the user gets a link to open a shared document. The welcome dialog of Collabora Online Development Edition (CODE) is not shown to guest users. Use IsAnonymousUser instead for 24.04.4 and newer.
