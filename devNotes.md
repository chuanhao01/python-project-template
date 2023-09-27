# Dev Notes

## Update installed package versions in the project

Both in the root project and in the generated template project, there is a Makefile command to help you "update" the dev dependencies used in the project. This is hard coded by design and making a universal bash script that is able to parse the `pyprojct.toml` to get this list of dependencies to update is non-trival. (Would require installing other CLI tools etc.) There is a possibility of making a python script to do the parsing in the future.

Alternatives are to update the dependencies manually or use a plugin like [poetry-plugin-up](https://github.com/MousaZeidBaker/poetry-plugin-up).
