var scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a162a);
var camera = new THREE.PerspectiveCamera(75, 800/600, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(800, 600);
renderer.sortObjects = false
document.body.appendChild(renderer.domElement);


var controls = new OrbitControls( camera, renderer.domElement );

controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.05;

controls.screenSpacePanning = false;

controls.minDistance = 1;
controls.maxDistance = 50;

var objects = [];
