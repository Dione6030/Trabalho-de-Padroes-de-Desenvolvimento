class tipoArvore {
    private _especie: string;
    private _textura: HTMLImageElement;
    private _cor: string;

    constructor(especie: string, textura: HTMLImageElement, cor: string) {
        this._especie = especie;
        this._textura = textura;
        this._cor = cor;
    }

    get especie(): string {
        return this._especie;
    }

    get textura(): HTMLImageElement {
        return this._textura;
    }

    get cor(): string {
        return this._cor;
    }

    set especie(value: string) {
        this._especie = value;
    }

    set textura(value: HTMLImageElement) {
        this._textura = value;
    }

    set cor(value: string) {
        this._cor = value;
    }

    public desenhar(x: number, y: number, z: number): void {
        console.log(`Desenhando árvore do tipo ${this._especie} na posição (${x}, ${y}, ${z}) com cor ${this._cor}`);
    }
}

class fabricarArvore {
    private arvoresTipo: Map<string, tipoArvore>;

    constructor() {
        this.arvoresTipo = new Map();
    }

    public pegarArvore(especie: string, textura: HTMLImageElement, cor: string) {
        const chave = `${especie}-${textura.src}-${cor}`;

        let tipo = this.arvoresTipo.get(chave);

        if (!tipo) {
            tipo = new tipoArvore(especie, textura, cor);
            this.arvoresTipo.set(chave, tipo);
        }
        return tipo;
    }
}

class ArvoreFly {
    public x: number;
    public y: number;
    public z: number;
    public tipo: tipoArvore;

    constructor(x: number, y: number, z: number, tipo: tipoArvore) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.tipo = tipo;
    }

    public desenhar(): void {
        this.tipo.desenhar(this.x, this.y, this.z);
    }
}

class FlorestaFly {
    private fabricarArvore: fabricarArvore;
    public arvores: ArvoreFly[];

    constructor() {
        this.arvores = [];
        this.fabricarArvore = new fabricarArvore();
    }

    public plantarArvore(x: number, y: number, z: number, especie: string, textura: HTMLImageElement, cor: string): ArvoreFly {
        const tipo = this.fabricarArvore.pegarArvore(especie, textura, cor);
        const arvore = new ArvoreFly(x, y, z, tipo);
        this.arvores.push(arvore);
        return arvore;
    }

    public desenhar(): void {
        this.arvores.forEach(arvore => arvore.desenhar());
    }
}