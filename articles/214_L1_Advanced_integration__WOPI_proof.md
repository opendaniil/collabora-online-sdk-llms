---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#wopi-proof"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "wopi-proof"
title: "WOPI proof"
canonical_title: "Advanced integration / WOPI proof"
toc_level: "1"
breadcrumbs: "Advanced integration / WOPI proof"
---
When processing WOPI requests from Collabora Online, sometimes it is desirable to verify that these requests are actually coming from the expected Collabora Online server. A common use case is when the access to a document is restricted, for example download is forbidden. If someone knows the WOPISrc and the access token, it is enough to get the whole file data, circumventing the protection. You can block WOPI-like protocol at the firewall, or IP filter on source in your server implementation, but the best practice is to use WOPI proof.

When the WOPI proof keypair is present in configuration, Collabora Online signs every WOPI request with the private key. The corresponding public key can be found in the proof-key element of the WOPI discovery XML. Each request includes the signature in the `X-WOPI-Proof` and `X-WOPI-ProofOld` HTTP headers.

The WOPI proof keypair is automatically generated when Collabora Online is installed from rpm or deb packages. In case of docker, the WOPI proof keypair is not part of the docker image, for obvious reasons. The docker image is public and giving away a pair of keys that anyone can have access to is not smart. In the docker case the WOPI proof keypair has to be generated and added as a volume to the container.

To generate WOPI proof keypair use the following command:

```
sudo coolconfig generate-proof-key
```

or if your configuration directory is not /etc, you can run ssh-keygen manually:

```
ssh-keygen -t rsa -N "" -m PEM -f /some/path/proof_key
```

Note

The proof_key file must be readable by the coolwsd process.
