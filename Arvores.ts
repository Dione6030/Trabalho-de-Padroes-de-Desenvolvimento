class Arvore {
    x: number;
    y: number;
    z: number;
    especie: string;
    textura: HTMLImageElement;
    cor: string;
    modelo: any;

    constructor(x: number, y: number, z: number, especie: string, textura: HTMLImageElement, cor: string, modelo: any) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.especie = especie;
        this.textura = textura;
        this.cor = cor;
        this.modelo = modelo;
    }
}

class Floresta {
    public arvores: Arvore[];
    
    constructor() {
        this.arvores = [];
    }

    public plantarArvore(arvore: Arvore): void {
        this.arvores.push(arvore);
    }
};