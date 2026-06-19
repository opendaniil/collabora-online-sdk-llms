---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/CODE_Docker_image.xhtml#how-to-configure-docker-image"
source_file: "docs/installation/CODE_Docker_image.xhtml"
source_anchor: "how-to-configure-docker-image"
title: "How to configure Docker image"
canonical_title: "Installation guide / CODE Docker image / How to configure Docker image"
toc_level: "2"
breadcrumbs: "Installation guide / CODE Docker image / How to configure Docker image"
---
There are multiple ways to put application configuration into Docker containers. Collabora Online has many configuration options and the Docker image comes with a built-in `/etc/coolwsd/coolwsd.xml` configuration file with the defaults.

### 1. Setting the application configuration dynamically via environment variables

After the `-e` command line option of `docker run` command you can define environment variables, that are passed to the container.

By default Collabora Online enables the first WOPI host that tries to connect. You can define the allowed WOPI hosts by passing environment variables.

`aliasgroup1=https://<domain1>:443,https://<your-dot-escaped-aliasname1>|<your-dot-escaped-aliasname2>:443`, `aliasgroup1`, `aliasgroup2`… and so on should be added as per the requirement. `<domain1>` is the WOPI host, i.e. your preferred File Sync and Share solution that implements the WOPI protocol, for example `share.example.com`. `<your-dot-escaped-aliasname1>|<your-dot-escaped-aliasname2>` are the aliasnames with which you can access the same WOPI host (in this case `<domain1>`) aliasnames can use regular expressions.If you don’t have any aliases, then only domain needs to be defined, for example `aliasgroup2=https://<domain2>:443`. With `aliasgroup1=https://.*:443` you can allow everyone to connect (public demo site).

Other optional environment variables that you can pass to the container at startup are the following:

| username | User name for the admin console |
| --- | --- |
| password | Password for the admin console |
| DONT_GEN_SSL_CERT | When this environment variable is set (is not “”), then startup script will not generate a new SSL certificate signed by a dummy CA. It is useful, if you want to use your own SSL certificate for some reason. |
| cert_domain | When this environment variable is set (is not “”), then startup script will generate a new SSL certificate signed by a dummy CA for this domain, not for localhost |
| server_name | When this environment variable is set (is not “”), then its value will be used as server name in /etc/coolwsd/coolwsd.xml. Without this, CODE is not delivering a correct host for the websocket connection in case of a proxy in front of it. |
| dictionaries | By default only limited set of spelling dictionaries and thesauri are configured for CODE, mainly for performance reasons. The default set of languages is the following: de_DE en_GB en_US es_ES fr_FR it nl pt_BR pt_PT ru. With the dictionaries environment variable you can change this list. The dictionaries environment variable should contain the space separated list of language codes (optionally followed by country code). In order to save resources, it makes sense to load only those dictionaries that are actually needed. |
| extra_params | You can pass extra command line parameters to coolwsd via this environment variable. For example, if you want to start coolwsd without SSL, when you test or develop, the syntax is: -e "extra_params=--o:ssl.enable=false". To learn about all possible options, refer to the self-documented /etc/coolwsd/coolwsd.xml configuration file in the Docker image. |

### 2. Use the configuration file directly

After starting the container, you can copy the configuration file out of the container (using `docker cp`), edit it, and copy it back to the container. It is also possible to mount the configuration file, and modify it outside of the container. The container will notice that the configuration file has changed, and the service will be restarted (don’t forget the `--restart always` option when you start the container with `docker run`).
