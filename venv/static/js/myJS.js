function getPic(ProgramName) {

}

function ts() {
    alert("还未开发，敬请期待!");
}
var thumbs = [];
        for (var i=0; i<104; i++) {
            thumbs.push({
                url: "http://tjenkinson.me/clappr-thumbnails-plugin/assets/thumbnails/thumb_"+(i+1)+".jpg",
                time: 1 + (i*2)
            });
        }
        var player = new Clappr.Player({
            source: "../static/videos/1.mp4",
            parentId: "#player",

            plugins: {
                core: [ClapprThumbnailsPlugin,ClapprMarkersPlugin],

            },
            scrubThumbnails: {
                backdropHeight: 64, // set to 0 or null to disable backdrop
                spotlightHeight: 84, // set to 0 or null to disable spotlight
                backdropMinOpacity: 0.4, // optional
               backdropMaxOpacity: 1, // optional
              thumbs: thumbs
            },
            markersPlugin: {
                markers: [
                  new ClapprMarkersPlugin.StandardMarker(0, "The beginning!"),
                  new ClapprMarkersPlugin.StandardMarker(90, "Something interesting."),
                 new ClapprMarkersPlugin.StandardMarker(450, "The conclusion.")
             ],
                tooltipBottomMargin: 17 // optional
        }

});
