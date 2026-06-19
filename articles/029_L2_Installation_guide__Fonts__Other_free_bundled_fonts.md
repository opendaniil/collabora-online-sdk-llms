---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Fonts.xhtml#other-free-bundled-fonts"
source_file: "docs/installation/Fonts.xhtml"
source_anchor: "other-free-bundled-fonts"
title: "Other free bundled fonts"
canonical_title: "Installation guide / Fonts / Other free bundled fonts"
toc_level: "2"
breadcrumbs: "Installation guide / Fonts / Other free bundled fonts"
---
| Font name | Reason to bundle |
| --- | --- |
| DejaVu | broad Unicode coverage |
| Gentium | for Latin, Cyrillic, and Greek scripts |
| Noto | full Unicode coverage |
| OpenDyslexic | by customer request |
| Open Sans | by customer request |
| Karla | used by Collabora internally |
| Linux Libertine G and Linux Biolinum G | rich typographic features, see https://www.numbertext.org/linux/ |
| Source Sans Pro | by customer request |
| Alef, David Libre, Frank Ruhl Hofshi, Miriam Libre, Rubik | for Hebrew script |
| Amiri, Reem Kufi, Scheherazade | for Arabic script |

When you install coolwsd package, the post-install script will look for additional fonts on your system, and install them for Collabora Online (in the systemplate). If you install fonts to your system after installing coolwsd, you need to [update the systemplate manually](030_L1_Installation_guide__Updating_systemplate.md) and restart coolwsd service.

You have the option to let Collabora online download fonts. This method does not require restart of the coolwsd service, remote fonts become available for new editing sessions within a minute. See the details in [Remote configuration](031_L1_Installation_guide__Configuration.md) chapter.

If you use docker you can also share fonts installed on the system using [docker volumes](https://docs.docker.com/engine/storage/volumes/) [https://docs.docker.com/engine/storage/volumes/], where `/opt/local/my-fonts` is where the fonts to share are, in the docker-compose section for Collabora Online container:

```
volumes:
  - /opt/local/my-fonts:/usr/share/fonts/truetype/more/
  - /opt/local/my-fonts:/opt/cool/systemplate/usr/share/fonts/truetype/more/
```

For Kubernetes you can checkout [Installing Custom Fonts](014_L1_Installation_guide__Collabora_Online_for_Kubernetes.md) chapter
