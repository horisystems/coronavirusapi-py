## coronavirusapi-py

Retrieve coronavirus current and historical [data](https://www.covid19api.dev).


### Getting Started

Run the commands below if you want to test it in a virtual environment: 

```sh
## Prerequisites
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install pip-tools

## Compile Requirements
pip-compile ./requirements.in

## Upgrade Package
pip-compile --upgrade-package requests

## Sync Packages
pip-sync
```

For instance, running this command would return coronavirus data for May 2021.

```sh
python3 example.py
```

Leave the virtual environment:

```sh
deactivate venv
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Cloudeya/coronavirusapi-wrapper/tags).

## License

This project is licensed under the [WTFPL License](LICENSE) - see the file for details.

## Copyright

(c) 2020 [Phooni Limited](https://phooni.com).
