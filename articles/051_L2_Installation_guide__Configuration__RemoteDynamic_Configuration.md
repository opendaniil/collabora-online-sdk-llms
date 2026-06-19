---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#remote-dynamic-configuration"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "remote-dynamic-configuration"
title: "Remote/Dynamic Configuration"
canonical_title: "Installation guide / Configuration / Remote/Dynamic Configuration"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Remote/Dynamic Configuration"
---
These changes can be now done without restarting Collabora server. Collabora server will request a JSON response to the remote server every 60 second and if there is new changes in JSON it will overwrite coolwsd.xml settings. Thus, adding the respective WOPI hosts and locked_hosts to the allow/deny list. The configuration will take effect the next time a document gets open.

Note

Collabora uses ETag header to identify whether the JSON is changed from last request or not. Therefore it is recommended to add ETag header in JSON response of remote server.

Important

With production versions only HTTPS protocol is allowed for security reasons.

### Enable remote server configuration by adding url

```
<remote_config >
  <remote_url desc="remote server to which you will send request to get remote config in response" type="string" default="">https://server_url_endpoint</remote_url>
</remote_config>
```

### JSON format

Configuration will be overwritten if JSON response has been changed

```
{
  "kind": "configuration",
  "remote_font_config":
  {
    "url": "https://.../fonts.json"
  },

  "storage":
  {
    "wopi":
    {
      "alias_groups":
      {
        "mode" : "groups",
        "groups":
        [
          { "host": "scheme://hostname:port", "allow": "true" , "aliases": ["scheme://aliasname1:port", "scheme://alias-regex-pattern:port”]},
        ]
      }
    }
  },

  "feature_locking":
  {
    "locked_hosts":
    {
      "allow":"true",
      "hosts":
      [
          { "host": "pattern1", "read_only": true, "disabled_commands": true },
          { "host": "pattern2", "read_only": false, "disabled_commands": true },
      ]
    },
    // unlock dialog customization
    "unlock_image": "https://<hostname>/static/<image_endpoint>",
    "translations":
      [
        {
          "language": "de",
          "unlock_title": "Gehen Sie zur Detailseite und entdecken Sie alle Funktionen:",
          "writer_unlock_highlights": "Überprüfen und schreiben Sie mit Leichtigkeit",
          "calc_unlock_highlights": "Machen Sie sich ein besseres Bild von Ihren Daten",
          "impress_unlock_highlights": "Bringen Sie Ihre nächste Präsentation auf den Punkt",
          "draw_unlock_highlights": "Zeichne und organisiere dich",
        },
        // more translations possible
      ]
  },
}
```

Please note that JSON response is checked every minute for changes. Every block in JSON is optional i.e. you can use any of the `remote_font_config`, `storage`, `feature_locking` JSON individually.

JSON config will overwrite values given in coolwsd.xml file i.e. `groups` tag will overwrite all host tags in wopi section. `locked_hosts` allow should be true to enable allow/deny feature_lock per WOPI host. If host pattern does not match for `locked_host`, the fallback setting will be applied. `unlock_image` and `translations` will overwrite respective xml:value pair in feature_locking section

### Enable download and availability of more fonts by pointing to a font configuration file

```
<remote_font_config>
    <url desc="URL of optional JSON file that lists fonts to be included in Online" type="string" default="">https://someserver/path/file.json</url>
</remote_font_config>
```

### Remote font configuration JSON format

The JSON file pointed to by the above should have contents like in this example

```
{
    "kind": "fontconfiguration",
    "server": "Some pretty name",
    "fonts": [
        {
            "uri": "https://somehost/path/f1.ttf"
        },
        {
            "uri": "https://someotherhost/path/f2.ttf",
            "stamp": "foo3"
        },
        {
            "uri": "https://whatever/path/x42.ttf"
        }
    ]
}
```

The JSON file is re-downloaded and scanned whenever it has changed. This is checked once a minute.

If an element in the fonts array has a `stamp` property then the font file will be re-downloaded and taken into use whenever the stamp has been changed. (And the old version of the font is forgotten.) The stamp can be any string, its contents is not interpreted in any way. The only thing checked is whether it changes. If no stamp property is provided, the web server in question is queried once a minute to check whether the font file has been updated.

The name of a font file is irrelevant. The name of the font is read from the contents of the file. The file should be a TrueType or OpenType font.

### AutoSave settings

New in version 24.04.

Since 24.04, by default, Cool saves documents that have unsaved changes every 5 minutes, and idle documents every 30 seconds. Saves are nearly instantaneous for users as saving is done out of the document process. This can be changed in `/etc/coolwsd/coolwsd.xml`, with the settings `autosave_duration_secs` and `idlesave_duration_secs`.
