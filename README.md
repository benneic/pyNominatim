pyNominatim
===========

A python client library for the Nominatim service provided by Open Street Map

```
Nominatim (from the Latin, 'by name') is a tool to search osm data by name and address and to generate synthetic addresses of osm points (reverse geocoding). It can be found at http://nominatim.openstreetmap.org .
```

## Usage

  ```python
  import pynominatim
  client = pynominatim.create()
  ```

### Search

  result = client.search('23 Foster Street, Surry Hills, NSW')

### Reverse

  result = client.search(-33.879858, 151.210046)