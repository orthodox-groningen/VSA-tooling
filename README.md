# Stap 135 - HTML-commentaar policy

Deze patch voert broncommentaar binnen VSA-notatie in.

Kort:

- `<!-- ... -->` blijft in de bron staan;
- parser/validator/renderers negeren het;
- SVG bevat geen commentaar of commentaartekst;
- oude SVG `plain-text` metadata-comments vervallen.
