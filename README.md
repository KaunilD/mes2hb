# Optical Density to Oxy and De-Oxy Hb [mes2hb]

Convert optical density data (red (< 700 nm) and infrared(>810nm)) from functional near infrared spectroscope (fNIRS) to oxy, de-oxy hemoglobin concentrations using modified Beer-Lambert law.

Built with python.

### Dependencies
 1. python 3.X
  2. numpy


### Installation

Install using [python](https://www.python.org/downloads/release/python-370/)

```sh
$ cd mes2hb
$ python setup.py install
```

### Usage

##### Example [without install]
* You can use this utility without any installation by executing the driver script -   `mes2hb-driver.py` located in the root of `mes2hb/`.

* For Example:
    ```python
    $ python mes2hb-driver.py
    ````

License
----

MIT