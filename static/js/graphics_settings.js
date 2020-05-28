var scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a162a);
var camera = new THREE.PerspectiveCamera(75, 800 / 600, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(800, 600);
renderer.sortObjects = false
document.body.appendChild(renderer.domElement);


var controls = new OrbitControls(camera, renderer.domElement);

controls.enableDamping = true;
controls.dampingFactor = 0.05;

controls.screenSpacePanning = false;

controls.minDistance = 1;
controls.maxDistance = 50;

controls.rotateLeft(3.14 / 3);
controls.rotateUp(3.14 / 6);

camera.position.x = 0;
camera.position.y = 0;
camera.position.z = 15;

document.addEventListener("keydown", onDocumentKeyDown, false);

function set_rotation(angle1, angle2) {
    camera.position.x = 0;
    camera.position.y = 0;
    camera.position.z = 15;
    controls.dropRotation();
    controls.rotateLeft(angle1);
    controls.rotateUp(angle2);
}

function onDocumentKeyDown(event) {
    if (event.which === 82) {
        set_rotation(3.14/3, 3.14/6);
    }
}

var objects = [];
