## Environment management

### Create the environment from `environment.yml`

```console
conda env create -f environment.yml
```


### Update `environment.yml` whenever new dependencies were installed

```console
conda env export --name wqu-capstone --file environment.yml
```

## Documentation management

### Adding pages to MkDocs documentation

Inside the `docs` directory, you may add new markdown files in which you describe individual components of the finished
total project. Make sure to add the names of the new markdown files to the `mkdocs.yml` file under the `nav` header.

### Running the MkDocs documentation

```console
mkdocs serve
```