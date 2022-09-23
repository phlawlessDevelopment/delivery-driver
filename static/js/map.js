(async () => {
  const zoom = 12;
  const center = [-3.211993851621597, 55.95032575687776];
  const southWest = [-3.4495326, 55.8187919];
  const northEast = [-3.0749512, 56.0040837];
  const maxBounds = [
    southWest, // Southwest coordinates
    northEast, // Northeast coordinates
  ];
  const response = await (
    await fetch(`${window.location.origin}/mapbox-token/`)
  ).json();

  mapboxgl.accessToken = response.token;
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center,
    zoom,
    maxBounds,
  });
  map.on("load", () => {
    // Load an image from an external URL.
    map.loadImage(
      `${window.location.origin}/static/img/arrow.png`,
      (error, image) => {
        if (error) throw error;

        // Add the image to the map style.
        map.addImage("arrow", image);

        // Add a data source containing one point feature.
        map.addSource("point", {
          type: "geojson",
          data: {
            type: "FeatureCollection",
            features: [
              {
                type: "Feature",
                geometry: {
                  type: "Point",
                  coordinates: center,
                },
              },
            ],
          },
        });

        // Add a layer to use the image to represent the data.
        map.addLayer({
          id: "points",
          type: "symbol",
          source: "point", // reference the data source
          layout: {
            "icon-image": "arrow", // reference the image
            "icon-size": 0.25,
            "icon-rotate": 90, //degrees
          },
        });
      }
    );
  });
  document.getElementById("pick-loc").onclick = async () => {
    const response = await (await fetch(`${window.location.origin}/random-location/`)).json();
    console.log(response);

  };
  document.getElementById('map').onclick = ()=>{
    
  }
})();
