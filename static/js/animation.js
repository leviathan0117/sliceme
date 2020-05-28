var parallelepiped = new Parallelepiped(2, 4, 8);

cut_points = [
    new THREE.Vector3(-1, -2, 3),
    new THREE.Vector3(1, -2, 3),
    new THREE.Vector3(1, 2, 0),
    new THREE.Vector3(-1, 2, 0)
]
parallelepiped.new_cut(new Cut(cut_points));

function animate() {
    controls.update();
}

animate();