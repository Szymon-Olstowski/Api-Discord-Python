from flask import Flask, render_template,request,redirect
import requests
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/users')
@app.route('/users',methods=['GET', 'POST'])
def users():
    class m:
        d=0
        ds=0
    ds=m.d
    d=m.d
    if request.method=='POST' and 'token' in request.form and 'userm' in request.form and 'id_serwer' in request.form:
        token=request.form['token']
        userm=request.form['userm']
        id_serwer=request.form['id_serwer']
        headers = {
            "Authorization":token
            }
        params1 = {
            "query": userm, #szukaj osoby
            }
        response1 = requests.get("https://discord.com/api/v10/guilds/"+id_serwer+"/members/search", headers=headers, params=params1)
        data1 = response1.json()[0]
        data1s = response1.json()[0]['user']
        m.ds=data1s
        m.d=data1
        d=m.d
        ds=m.ds
    return render_template('users.html',d=d,ds=ds)
@app.route('/channel',methods=['GET', 'POST'])
def channel():
    tab=[]
    if request.method=='POST' and 'token' in request.form and 'key_api' in request.form:
        token=request.form['token']
        key_api=request.form['key_api']
        headers = {
            "Authorization":token
            }
        response2=requests.get("https://discord.com/api/v10/guilds/"+key_api+"/channels",headers=headers)
        data2=response2.json()
        a=len(data2)
        for i in range(0,a):
            match data2[i]["type"]:
                case 0:
                    tab.append(str(data2[i]['name']+" Kanał tekstowy"))
                case 1:
                    tab.append(str(data2[i]['name']+" Wiadomość DM"))
                case 2:
                    tab.append(str(data2[i]['name']+ " Kanał głosowy"))
                case 3:
                    tab.append(str(data2[i]['name']+" Grupowy DM"))
                case 4:
                    tab.append(str(data2[i]['name']+" Kategoria"))
                case 5:
                    tab.append(str(data2[i]['name']+" Kanał Informacyjny"))
                case 10:
                    tab.append(str(data2[i]['name']+" Tymczasowy podkanał"))
                case 11:
                    tab.append(str(data2[i]['name']+" Tymczasowy podkanał w text"))
                case 12:
                    tab.append(str(data2[i]['name']+ " Kanał tylko dla odpowiednich permisji"))
                case 13:
                    tab.append(str(data2[i]['name']+ "Kanał głosowy publiczny"))
                case 14:
                    tab.append(str(data2[i]['name']+" Kanał zawiracjących liście serwerów"))
                case 15:
                   tab.append(str(data2[i]['name']+" Kanał zawierający wątki"))
    return render_template('channel.html',tab=tab)
@app.route('/logs',methods=['GET', 'POST'])
def logs():
    tas=[]
    tas1=[]
    data3=0
    if request.method=='POST' and 'token' in request.form and 'key_api' in request.form:
        token=request.form['token']
        key_api=request.form['key_api']
        headers = {
            "Authorization":token
            }
        response3=requests.get("https://discord.com/api/v10/guilds/"+key_api+"/audit-logs",headers=headers)
        data3=response3.json()['integrations']
        data3s=response3.json()['audit_log_entries']
        a=len(data3)
        ai=len(data3s)
        print(data3s)
        for i in range(0,a):
            tas.append("id: "+str(data3[i]['id'])+ "\nNazwa: "+str(data3[i]['name'])+"\nTyp: "+str(data3[i]['type'])+"\nNazwa konta: "+str(data3[i]['account']['name'])+"\nId: "+str(data3[i]['account']['id'])+"\nAplikcja id: "+str(data3[i]['application_id']))
        for i in range(0,ai):
            tas1.append(data3s[i])
        

    return render_template('logs.html',tas=tas,tas1=tas1)
if __name__ == '__main__':
    app.run(host='127.0.0.1') #wprawadź api swojego komputera