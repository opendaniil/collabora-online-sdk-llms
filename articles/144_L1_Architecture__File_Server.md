---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#file-server"
source_file: "docs/architecture.xhtml"
source_anchor: "file-server"
title: "File Server"
canonical_title: "Architecture / File Server"
toc_level: "1"
breadcrumbs: "Architecture / File Server"
---
CoolWSD acts as a file server, in addition to being the server component that handles document loading, editing, saving, etc. The file server in CoolWSD serves only known files. That is, the files are known in advance, enumerated, read from disk, loaded into an in-memory cache, all during starting up and initializing the server.

This has a number of benefits, beyond performance. First, only the known directory (browser/dist) is served from. This avoids the risk of exposing any files outside of the known directory. Second, files that should not be served (for any reason) are detected and excluded at start up. In addition, the file server is responsible for serving service-specific files, such as hosting and discovery, as well as `favicon.ico`, `robots.txt`, etc.

Once the file server is initialized, it can serve only the files that it has cached in memory. All other requests are ignored, with proper error logged and an HTTP error code returned (such as 403 or 404).

File serving is exclusively done over HTTP and HTTPS only. The only HTTP supported verbs are GET and POST. GET is used for file serving while POST is exclusively for interacting with documents. For example, converting, downloading, etc.

The reason for using POST for document interactions is to pass the authentication key, which is used to authenticate the user against the storage server and against accessing the document in question, is safest when transmitted in the body of the request rather than in the address, as GET would do.

Finally, for loading documents and for the connection between the server and client, the HTTP socket is upgraded to WebSocket, which is used for the duration of the session that a user has on a document.
