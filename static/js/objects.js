class Cut {
    constructor(points_array) {
        this.geometry_main = new THREE.Geometry();
        this.geometry_main.vertices = points_array;
        for (var i = 0; i < points_array.length - 2; i++) {
            this.geometry_main.faces.push(
                new THREE.Face3(0, i + 1, i + 2)
            );
        }
        this.material_main = new THREE.MeshBasicMaterial({
            color: 0xff0000, opacity: 0.6, transparent: 1,
            side: THREE.DoubleSide, depthWrite: false
        });

        this.mesh = new THREE.Mesh(this.geometry_main, this.material_main);

        objects.push(this)
    }

    add_opaque() {
        //nothing opaque
    }

    add_transparent() {
        scene.add(this.mesh);
    }

    add_to_rotation(rotation_addition) {
        this.mesh.rotation.x += rotation_addition[0]
        this.mesh.rotation.y += rotation_addition[1]
        this.mesh.rotation.z += rotation_addition[2]
    }
}

class Parallelepiped {
    constructor(height, width, depth) {

        this.geometry_main = new THREE.Geometry();
        this.geometry_lines = new THREE.Geometry();
        this.geometry_cuts = [];
        this.fill_geometry(height, width, depth)

        this.material_main = new THREE.MeshBasicMaterial({
            color: 0x005500, opacity: 0.3, transparent: 1,
            side: THREE.DoubleSide, depthWrite: false
        });
        this.material_lines = new THREE.MeshBasicMaterial({color: 0x00ff00});

        this.mesh = new THREE.Mesh(this.geometry_main, this.material_main);
        this.line = new THREE.LineSegments(this.geometry_lines, this.material_lines);

        objects.push(this)
    }

    fill_geometry(height, width, depth) {
        this.geometry_main.vertices.push(
            new THREE.Vector3(-height / 2, -width / 2, -depth / 2),
            new THREE.Vector3(height / 2, -width / 2, -depth / 2),
            new THREE.Vector3(height / 2, width / 2, -depth / 2),
            new THREE.Vector3(-height / 2, width / 2, -depth / 2),
            new THREE.Vector3(-height / 2, -width / 2, depth / 2),
            new THREE.Vector3(height / 2, -width / 2, depth / 2),
            new THREE.Vector3(height / 2, width / 2, depth / 2),
            new THREE.Vector3(-height / 2, width / 2, depth / 2),
        );
        this.geometry_main.faces.push(
            new THREE.Face3(0, 1, 2),
            new THREE.Face3(0, 2, 3),
            new THREE.Face3(0, 4, 5),
            new THREE.Face3(0, 5, 1),
            new THREE.Face3(1, 5, 6),
            new THREE.Face3(1, 6, 2),
            new THREE.Face3(2, 6, 7),
            new THREE.Face3(2, 7, 3),
            new THREE.Face3(3, 7, 4),
            new THREE.Face3(3, 4, 0),
            new THREE.Face3(4, 5, 6),
            new THREE.Face3(4, 6, 7)
        );
        this.geometry_lines.vertices.push(
            this.geometry_main.vertices[0], this.geometry_main.vertices[1],
            this.geometry_main.vertices[1], this.geometry_main.vertices[2],
            this.geometry_main.vertices[2], this.geometry_main.vertices[3],
            this.geometry_main.vertices[3], this.geometry_main.vertices[0],
            this.geometry_main.vertices[1], this.geometry_main.vertices[5],
            this.geometry_main.vertices[2], this.geometry_main.vertices[6],
            this.geometry_main.vertices[3], this.geometry_main.vertices[7],
            this.geometry_main.vertices[0], this.geometry_main.vertices[4],
            this.geometry_main.vertices[4], this.geometry_main.vertices[5],
            this.geometry_main.vertices[5], this.geometry_main.vertices[6],
            this.geometry_main.vertices[6], this.geometry_main.vertices[7],
            this.geometry_main.vertices[7], this.geometry_main.vertices[4]
        );
    }

    add_opaque() {
        scene.add(this.line);
    }

    add_transparent() {
        scene.add(this.mesh);
    }

    new_cut(cut) {
        this.geometry_cuts.push(cut);
    }

    add_to_rotation(rotation_addition) {
        this.line.rotation.x += rotation_addition[0]
        this.line.rotation.y += rotation_addition[1]
        this.line.rotation.z += rotation_addition[2]

        this.mesh.rotation.x += rotation_addition[0]
        this.mesh.rotation.y += rotation_addition[1]
        this.mesh.rotation.z += rotation_addition[2]

        for (var i = 0; i < this.geometry_cuts.length; i++) {
            this.geometry_cuts[i].add_to_rotation(rotation_addition);
        }
    }
}


var parallelepiped = new Parallelepiped(2, 4, 8);

cut_points = [
    new THREE.Vector3(-1, -2, 3),
    new THREE.Vector3(1, -2, 3),
    new THREE.Vector3(1, 2, 0),
    new THREE.Vector3(-1, 2, 0)
]
parallelepiped.new_cut(new Cut(cut_points));