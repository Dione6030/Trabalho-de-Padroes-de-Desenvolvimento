class Arvore {
    x: number;
    y: number;
    z: number;
    especie: string;
    textura: HTMLImageElement;
    cor: string;

    constructor(x: number, y: number, z: number, especie: string, textura: HTMLImageElement, cor: string) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.especie = especie;
        this.textura = textura;
        this.cor = cor;
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