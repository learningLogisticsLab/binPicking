# obj2stl

This project aims to be a simple and lightweight 3D model format converter from `obj` to `stl`

This project is written in python3.

  - [Install](#install)
  - [usage](#usage)
  - [List of all supported formats](#formats)


# Install

`sudo pip install obj2stl`


## usage

```
from obj2stl import obj2stl

obj2stl.convert(input='sample.obj',output='sample2.stl')
```

## Formats
Here is the list of all the supported formats
  - Wavefront `.obj`
  - STL files `.stl`

