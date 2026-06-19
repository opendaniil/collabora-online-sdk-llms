---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Updating__systemplate.xhtml"
source_file: "docs/installation/Updating__systemplate.xhtml"
source_anchor: ""
title: "Updating systemplate"
canonical_title: "Installation guide / Updating systemplate"
toc_level: "1"
breadcrumbs: "Installation guide / Updating systemplate"
---
Each document is isolated in its own `chroot` jail running its own instance of a LibreOfficeKit process, and runs as a non-privileged “cool” user. These `chroot` jails contain only the bare minimum of files (libraries, fonts, etc.) needed for running Collabora Office (LibreOfficeKit). The template of the jails is called systemplate, it is located at `/opt/cool/systemplate`, and it is generated after installation of the coolwsd package. The systemplate is also re-generated after installing updates of packages that are in use in systemplate (on RPM based systems) or after a successful apt update (on DEB based systems).

However, it is possible that the user wants to build systemplate manually, for example when new fonts are installed, or a security update of system libraries is deployed by other means. Perform the following command as root user.

In Collabora Online :

```
coolconfig update-system-template
```
