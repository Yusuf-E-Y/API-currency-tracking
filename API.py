from flask import Flask ,render_template
import Statistics

app = Flask(__name__)

usd_graph = Statistics.Create_graph(Statistics.dates_usd, Statistics.sales_usd, "USD sale price")
eur_graph = Statistics.Create_graph(Statistics.dates_eur, Statistics.sales_eur, "EUR sale price")
chf_graph = Statistics.Create_graph(Statistics.dates_chf, Statistics.sales_chf, "CHF sale price")

@app.route('/')
def home():
    dolar = Statistics.sales_usd[-1]
    euro = Statistics.sales_eur[-1]
    chf = Statistics.sales_chf[-1]
    
    usd_graph = Statistics.Create_graph(Statistics.dates_usd, Statistics.sales_usd, "USD sale price")
    eur_graph = Statistics.Create_graph(Statistics.dates_eur, Statistics.sales_eur, "EUR sale price")
    chf_graph = Statistics.Create_graph(Statistics.dates_chf, Statistics.sales_chf, "CHF sale price")
    linear_graph = Statistics.Create_graph_linear(6)

    aud = Statistics.aud_info
    cad = Statistics.cad_info
    gbp = Statistics.gbp_info

    situation = (170 * dolar) + (240 * euro)

    return render_template("index.html", 
                           dolar=dolar, 
                           euro=euro ,
                           usd_graph=usd_graph,
                           eur_graph=eur_graph,
                           chf_graph=chf_graph,
                           linear_graph=linear_graph,
                           chf=chf,
                           aud=aud,
                           cad=cad,
                           gbp=gbp,
                           situation=situation)

@app.route('/')
def about():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)