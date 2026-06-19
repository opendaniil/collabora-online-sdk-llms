---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#file-system"
source_file: "docs/architecture.xhtml"
source_anchor: "file-system"
title: "File System"
canonical_title: "Architecture / File System"
toc_level: "1"
breadcrumbs: "Architecture / File System"
---
WSD is given childroot argument through config (child_root_path). This is the root directory of jailed FS. This path can be anywhere, but here we’ll designate it as:

```
/childroot
```

Before spawning a ForKit instance, WSD needs to generate a random Jail-ID to use as the jail directory name. This `JailID` is then passed to ForKit as argument `jailid`.

Note: for security reasons, this directory name is randomly generated and should not be given out to the client. Since there is only one ForKit per WSD instance, there is also one `JailID` between them.

The ForKit creates a chroot in this directory (the jail directory):

```
/childroot/jailid/
```

ForKit copies the LO `instdir` (essentially installs LO in the chroot), then copies the Kit binary into the jail directory upon startup. Once done, it chroot-s and drops caps.

ForKit then waits on a read pipe to which WSD writes when a new request from a client is received. ForKit is responsible for spawning (or forking) Kit instances. For our purposes, it doesn’t matter whether Kit is spawned or forked.

Every document is hosted by a Kit instance. Each document is stored in a dedicated directory within the jail directory. The document root within the jail is /user/docs. The absolute path on the system (which isn’t accessible to the Kit process as it’s jailed) is:

```
/childroot/jailid/user/docs
```

Within this path, each document gets its own sub-directory based on another random Child-ID (which could be the Process ID of the Kit). This ChildId will be given out to clients to facilitate the insertion and downloading of documents. (Although strictly speaking the client can use the main document URI as key, this is the current design.)

```
/childroot/jailid/user/docs/childid
```
