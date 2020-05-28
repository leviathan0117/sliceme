for (var i = 0; i < objects.length; i++) {
    objects[i].add_opaque();
}
for (var i = 0; i < objects.length; i++) {
    objects[i].add_transparent();
}

function graphics_loop() {
    requestAnimationFrame(graphics_loop);

    animate(); // in animation.js

    renderer.render(scene, camera);
}

graphics_loop();