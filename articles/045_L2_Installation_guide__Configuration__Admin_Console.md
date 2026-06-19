---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#admin-console"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "admin-console"
title: "Admin Console"
canonical_title: "Installation guide / Configuration / Admin Console"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Admin Console"
---
You can do live monitoring of all the user sessions running on Collabora Online instance. The Admin Console URL is:

```
https://*hostname*:*port*/browser/dist/admin/admin.html
```

Port is `9980` by default. It will ask for username and password which is set in the admin_console block of `/etc/coolwsd/coolwsd.xml` or by `--o:admin_console.username=username` and `--o:admin_console.password=password` in coolwsd command line. You must set username and password. Admin Console is disabled if either of these are not set.

Note

It is possible to set up a password that is stored as salted hash in the config file, instead of plain text. This is the recommended way to set up password for the Admin Console. Use the `coolconfig` utility. `coolconfig set-admin-password` will ask for a user name and a password interactively on the terminal.

New in version 24.04.10.2: The command line options `--user` and `--password` allow specifying the authentication information on the command line. This is particulary useful for automatic deployment tools.

Note

There is support for authentication with `PAM`, if it is set up for coolwsd in the system. For example, with a simple `/etc/pam.d/coolwsd` config below, the user which runs coolwsd (‘cool’ in production environment) can login to admin console with normal linux password.

```
1 auth required pam_unix.so
2 account required pam_unix.so
```

After entering the correct password you should be able to monitor the live documents opened, total users, memory consumption, document URLs with number of users viewing that document etc. You can also kill the documents directly from the panel which would result in closing the socket connection to the respective document.

The admin-console front-end presents and fetches its data via a defined web socket protocol, which can be used to collect information programatically to integrate with other monitoring and control solutions. For the websocket protocol details of Admin Console, see the Admin Console section in the protocol documentation:

[https://github.com/CollaboraOnline/online/blob/main/wsd/protocol.txt](https://github.com/CollaboraOnline/online/blob/main/wsd/protocol.txt) .

It is simple to subscribe to receive client notifications, query the open documents and change server settings.
