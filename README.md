## Contributing a Model

1. Put the model's `.ttl` file in the `models/` directory
2. Create a `.md` file *with the same base name as the `.ttl` file* in the `examples/` directory:
    - This `.md` file should have at least the following 3 *empty* sections, in this order:
    - `## Downloads`
    - `## Queries`
    - `## Model Components`
3. Add this `.md` file to the `_toc.yml` file under the appropriate section (Building or System)
4. If you want to add queries to the model, add them in `queries.toml`. The section name should have the same base name as the `.ttl` and `.md` file.


### Example

For a model called `mybuilding.ttl`, the following files would be created:
- `models/mybuilding.ttl`
- `examples/mybuilding.md`

The `examples/mybuilding.md` file would look like this:

```
# My Example Building

<description of the building>

## Downloads

## Queries

## Model Components
```

The `queries.toml` file might look like this:

```toml
[[mybuilding]]
description="Zone/room temperature sensors"
query="""
SELECT ?location ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* s223:Sensor .
    ?sensor s223:observes ?property .
    ?property qudt:hasQuantityKind quantitykind:Temperature .
    ?sensor s223:hasObservationLocation ?location
}
"""
```
