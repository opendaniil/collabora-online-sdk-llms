---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#userprivateinfo"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "userprivateinfo"
title: "UserPrivateInfo"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / UserPrivateInfo"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / UserPrivateInfo"
---
JSON object that contains additional info about the user, but unlike the `UserExtraInfo` it is not shared among the views in collaborative editing sessions.

For example it can hold the `ZoteroAPIKey` which is the personal API key to Zotero Web API, for working with citation databases. When the integration provides a Zotero API key for the user, the functionality of handling Zotero databases gets enabled in Collabora Online’s user interface.

#### Document signing

When the `SignatureCert`, `SignatureKey` and `SignatureCa` keys in `UserPrivateInfo` are specified, the document signing functionality gets enabled in Collabora Online’s user interface.

For testing purposes it is OK to use self signed certificates. You can create the necessary files yourself. The following example creates a test CA, a test intermediate CA and a test certificate for document signing. The resulting `.pem` files provide the value for the above JSON keys.

To create the test root CA:

```
1 mkdir -p ca/{certs,crl,newcerts,private}
2 touch ca/index.txt
3 echo 1000 > ca/serial
4 curl -o ca/openssl.cnf https://raw.githubusercontent.com/CollaboraOnline/collabora-online-sdk-examples/master/signing/root.cnf
5 openssl genrsa -out ca/private/ca.key.pem 4096
6 openssl req -config ca/openssl.cnf -key ca/private/ca.key.pem -new -x509 -days 36500 -sha256 -extensions v3_ca -out ca/certs/ca.cert.pem -subj "/C=UK/ST=England/O=COOL Test/CN=COOL Test Root CA"
```

To create the test intermediate CA:

```
1 mkdir -p ca/intermediate/{certs,crl,csr,newcerts,private}
2 touch ca/intermediate/index.txt
3 echo 1000 > ca/intermediate/serial
4 curl -o ca/intermediate/openssl.cnf https://raw.githubusercontent.com/CollaboraOnline/collabora-online-sdk-examples/master/signing/intermediate.cnf
5 openssl genrsa -out ca/intermediate/private/intermediate.key.pem
6 openssl req -config ca/intermediate/openssl.cnf -new -sha256 -key ca/intermediate/private/intermediate.key.pem -out ca/intermediate/csr/intermediate.csr.pem -subj "/C=UK/ST=England/O=COOL Test/CN=COOL Test Intermediate CA"
7 openssl ca -batch -config ca/openssl.cnf -extensions v3_intermediate_ca -days 36500 -notext -md sha256 -in ca/intermediate/csr/intermediate.csr.pem -out ca/intermediate/certs/intermediate.cert.pem
8 cat ca/intermediate/certs/intermediate.cert.pem ca/certs/ca.cert.pem > ca/intermediate/certs/ca-chain.cert.pem
```

To create the signing certificate:

```
1 openssl genrsa -out ca/intermediate/private/example-cool-Alice.key.pem 2048
2 openssl req -config ca/intermediate/openssl.cnf -key ca/intermediate/private/example-cool-Alice.key.pem -new -sha256 -out ca/intermediate/csr/example-cool-Alice.csr.pem -subj "/C=UK/ST=England/O=COOL Test/CN=COOL Test Alice"
3 openssl ca -batch -config ca/intermediate/openssl.cnf -extensions usr_cert -days 36500 -notext -md sha256 -in ca/intermediate/csr/example-cool-Alice.csr.pem -out ca/intermediate/certs/example-cool-Alice.cert.pem
```

After these, you can find the CA chain at `ca/intermediate/certs/ca-chain.cert.pem`, the signing certificate at `ca/intermediate/certs/example-cool-Alice.cert.pem` and finally the signing key at `ca/intermediate/private/example-cool-Alice.key.pem`.
