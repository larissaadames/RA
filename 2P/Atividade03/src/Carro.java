public class Carro {
    private String modelo;
    private int ano;
    private String motor;
    private String cor;

    public Carro(){
        this.modelo = "modelo";
        this.ano = 0000;
        this.motor = "motor";
        this.cor = "cor";
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        if modelo
        this.modelo = modelo;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getMotor() {
        return motor;
    }

    public void setMotor(String motor) {
        this.motor = motor;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }
}
