---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#feature-locking"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "feature-locking"
title: "Feature Locking"
canonical_title: "Installation guide / Configuration / Feature Locking"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Feature Locking"
---
Collabora Online provides a way to lock the user out from using certain features or make them read-only users. When a user clicks on a feature that is locked, the user will be prompted with a popup with details about unlocking. To disable any feature you can specify its UNO command in the `locked_commands` field. When a locked user is treated with read-only permission `locked_commands` option is ignored. Other related options can be found in coolwsd.xml. To mark a user locked, the WOPI client should return `CheckFileInfo` containing a field `IsUserLocked` with a boolean value. To make the locked users read-only set `is_lock_readonly` setting to true.

### To allow/deny feature_lock per WOPI host:

```
<locked_hosts desc="Allow/deny feature-locked hosts. When allowed, the below host specification overrides the CheckFileInfo response." allow="true">
  <fallback desc="What to do if the given host is not covered by any rule in locked_hosts" read_only="true" disabled_commands="true"/>
  <host desc="Regex pattern of hostname to set as full-featured or locked." read_only="false" disabled_commands="false">pattern1</host>
</locked_hosts>
```

Please note that locked_hosts allow should be true to enable allow/deny feature_lock per WOPI host. If host pattern does not match for locked_host the fallback setting will be applied. This also overwrites the `isUserLocked` CheckFileInfo response.

**case-1:**`isUserLocked``locked_hosts``allow=true``locked_hosts``locked_hosts``fallback`**case-2:**`is_lock_readonly``true``locked_host``disabled_commands`

Note

This is not available in CODE.
