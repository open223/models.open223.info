---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: open223-models
  language: python
  name: open223-models
---
# LBNL Example SMB Radiant

This is a reference model provided by LBNL of a medium office building using a radiant system. Labels have been anonymized, and may not be interpretable.

## Downloads

- <a href="/compiled/lbnl-example-radiant.ttl">Turtle file (compiled)</a>
- <a href="/withimports/lbnl-example-radiant.ttl">Turtle file (with all imports)</a>
- <a href="/lbnl-example-radiant.ttl">Turtle file (original)</a>
- <a href="/lbnl-example-radiant.jsonld">JSON-LD file (original)</a>

<details>
<summary>What are these files?</summary>

- **Turtle file (original)**: This is the original source Turtle file that was provided to `models.open223.info`, usually as the output of some model creation tool.
- **Turtle file (compiled)**: This is the original Turtle file with all inferred relationships and values added through SHACL inference against the 223P ontology and other dependencies. **You should use this file for any further processing.** It does not contain any of the ontologies.
- **Turtle file (with all imports)**: This is the compiled Turtle file with all imports included in the file (223P ontology, QUDT ontology, and others). This is helpful when you do not want to deal with downloading and managing ontology dependencies. It is also much larger than the compiled file.
- **JSON-LD file (original)**: This is the original Turtle file converted to the JSON-LD format.

[Turtle](https://www.w3.org/TR/turtle/) is a syntax for RDF (Resource Description Framework) that is easy to read and write. It is a popular format for representing linked data. Parsers and serializers
are available in many programming languages. [JSON-LD](https://json-ld.org) is a JSON-based format for linked data that is easy to use with JavaScript and other web technologies.
</details>
    
## Queries
| Description | Query URL |
|-------------|-----------|
| Select all triples from model. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+%0ASELECT+%2A+WHERE+%7B%0A%09+%3Fs+%3Fp+%3Fo+%0A%7D%0A+LIMIT+10&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Flbnl-example-radiant.ttl'>Query Link</a> |

## Model Components
