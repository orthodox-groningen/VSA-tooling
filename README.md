# VSA stap 6 - meerdere fouten rapporteren

Deze stap verbetert `vsa validate`.

Nieuw:

- meerdere syntaxfouten verzamelen;
- meerdere semantische fouten verzamelen;
- niet stoppen bij de eerste fout;
- foutlijst geschikt maken voor CMD, Hugo en GitHub Actions.

Belangrijk:

- parsing zelf kan nog steeds stoppen bij een harde parsefout;
- maar de validatierunner doet eerst een recoverable syntax-scan;
- daarna wordt semantiek alleen uitgevoerd als er geen syntaxfouten zijn.

Dit voorkomt misleidende vervolgmeldingen.
