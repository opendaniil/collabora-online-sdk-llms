---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Installation_from_packages.xhtml#the-installation-procedure"
source_file: "docs/installation/Installation_from_packages.xhtml"
source_anchor: "the-installation-procedure"
title: "The Installation Procedure"
canonical_title: "Installation guide / Installation from packages / The Installation Procedure"
toc_level: "2"
breadcrumbs: "Installation guide / Installation from packages / The Installation Procedure"
---
On all the supported platforms, the installation procedure consist of three steps:

- Import of the signing key
- The installation itself
- Starting of the service, and enabling it for auto-start after reboot

### Collabora’s Partner

If you are Collabora’s Partner, please log into [The Partner portal](https://support.collaboraoffice.com/) [https://support.collaboraoffice.com/] get your unique secret URL from the Partner portal and follow the instructions listed there.

### CODE

If you are **not** Collabora’s Partner please follow [CODE instructions](https://www.collaboraonline.com/code/#learnmorecode) [https://www.collaboraonline.com/code/#learnmorecode]

### Distro-specific Installation Instructions

To install Collabora Office you need system administrator (root) privileges. The following command line examples are supposed to be entered from a system administrator (root) account. Alternatively you can use sudo.

```
export customer_hash=Example-413539ece39485afc35b4a469adfde0a279d2fd2
```

#### Debian, Ubuntu, other deb based Linux distribution

Please type the following commands into the shell as root:

1. download the signing key
  > ```
  > cd /usr/share/keyrings
  > wget https://collaboraoffice.com/downloads/gpg/collaboraonline-release-keyring.gpg
  > ```
2. add the repository to /etc/apt/sources.list.d
  > ```
  > cat << EOF > /etc/apt/sources.list.d/collaboraonline.sources
  > Types: deb
  > URIs: https://www.collaboraoffice.com/repos/CollaboraOnline/24.04/customer-deb-$customer_hash
  > Suites: ./
  > Signed-By: /usr/share/keyrings/collaboraonline-release-keyring.gpg
  > EOF
  > ```
3. perform the installation
  > ```
  > apt update && apt install coolwsd collabora-online-brand
  > ```

After successful installation, please follow the chapter [Configuration](031_L1_Installation_guide__Configuration.md).

#### RHEL, CentOS, and their derivatives

Please type the following commands into the shell as root:

1. import the signing key
  > ```
  > wget https://collaboraoffice.com/repos/CollaboraOnline/24.04/customer-rpm-$customer_hash/repodata/repomd.xml.key && rpm --import repomd.xml.key
  > ```
2. add the repository URL to yum
  > ```
  > yum-config-manager --add-repo https://collaboraoffice.com/repos/CollaboraOnline/24.04/customer-rpm-$customer_hash
  > ```
3. perform the installation
  > ```
  > yum install coolwsd collabora-online-brand
  > ```

After successful installation, please follow the chapter [Configuration](031_L1_Installation_guide__Configuration.md).

#### SLES 15 / openSUSE Leap 15.x

Please type the following commands into the shell as root:

1. import the signing key
  > ```
  > wget https://collaboraoffice.com/repos/CollaboraOnline/24.04/customer-rpm-$customer_hash/repodata/repomd.xml.key && rpm --import repomd.xml.key
  > ```
2. add the repository URL to zypper
  > ```
  > zypper ar -t yum
  > "https://collaboraoffice.com/repos/CollaboraOnline/24.04/customer-rpm-$customer_hash"
  > "Collabora Online"
  > ```
3. perform the installation
  > ```
  > zypper ref && zypper in coolwsd collabora-online-brand
  > ```

After successful installation, please follow the chapter [Configuration](031_L1_Installation_guide__Configuration.md).

### How to upgrade

If you are upgrading from Collabora Online 6.4 or earlier version to version 21.11 or newer, please read [Upgrade to Collabora Online 21.11](https://www.collaboraonline.com/upgrade-to-collabora-online-21.11/) [https://www.collaboraonline.com/upgrade-to-collabora-online-21.11/]. Otherwise it is enough to change the version number in the repository URL and upgrade as usual with the respective package manager. Although upgrade process is safe, it is always a good idea to backup configuration files in `/etc/coolwsd/` just in case.

### Localization

For complete user interface localization you need to install Collabora Office language resources. They are not direct dependencies of coolwsd. For example for German dialogs on Debian/Ubuntu:

```
apt install collaboraoffice*de
```

### Spelling dictionaries and thesauri

Collabora Online can use internal spelling dictionaries and thesauri (`collaboraoffice*-dict-*` packages). Collabora Online can use system spelling dictionaries and thesauri, too, that are located in `/usr/share/hunspell` and `/usr/share/mythes` directories.

Additionally, and starting with version 22.05, it’s possible to enable support for external grammar checking using [LanguageTool](https://languagetool.org/premium?a=collabora) [https://languagetool.org/premium?a=collabora]. For information please consult [Language Tool](079_L0_Grammar_checker_LanguageTool.md).
