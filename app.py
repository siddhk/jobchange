import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('lgboost.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    citydev = request.form.get('citydev')
    g = request.form.get('gender')
    gm=0
    gu=0
    gf=0
    go=0
    if g=='1':
        gm=1
        gf=0
        go=0
        gu=0
    elif g=='2':
        gm=0
        gf=1
        go=0
        gu=0
    elif g=='3':
        gm=0
        gf=0
        go=1
        gu=0
    r = request.form.get('relevent')
    e = request.form.get('enrollment')
    en=0
    ep=0
    ef=0
    eu=0
    if e=='1':
        en=1
        ep=0
        ef=0
        eu=0
    elif e=='2':
        en=0
        ep=1
        ef=0
        eu=0
    elif e=='3':
        en=0
        ep=0
        ef=1
        eu=0
    ed = request.form.get('edlevel')
    edm=0
    edg=0
    edpr=0
    edhs=0
    edphd=0
    if ed=='1':
        edm=1
        edg=0
        edpr=0
        edhs=0
        edphd=0
    elif ed=='2':
        edm=0
        edg=1
        edpr=0
        edhs=0
        edphd=0
    elif ed=='3':
        edm=0
        edg=0
        edpr=1
        edhs=0
        edphd=0
    elif ed=='4':
        edm=0
        edg=0
        edpr=0
        edhs=1
        edphd=0
    elif ed=='5':
        edm=0
        edg=0
        edpr=0
        edhs=0
        edphd=1    
    md = request.form.get('major')
    mdn=0
    mda=0
    mdh=0
    mds=0
    mdb=0
    mdo=0
    if md=='1':
        mdn=1
        mda=0
        mdh=0
        mds=0
        mdb=0
        mdo=0
    elif md=='2':
        mdn=0
        mda=1
        mdh=0
        mds=0
        mdb=0
        mdo=0
    elif md=='3':
        mdn=0
        mda=0
        mdh=1
        mds=0
        mdb=0
        mdo=0
    elif md=='4':
        mdn=0
        mda=0
        mdh=0
        mds=1
        mdb=0
        mdo=0
    elif md=='5':
        mdn=0
        mda=0
        mdh=0
        mds=0
        mdb=1
        mdo=0
    elif md=='5':
        mdn=0
        mda=0
        mdh=0
        mds=0
        mdb=0
        mdo=1
    exp = request.form.get('experience')
    cs= request.form.get('comsize')
    cs10=0
    cs50=0
    cs100=0
    cs500=0
    cs1000=0
    cs5000=0
    cs10000=0
    csg10000=0
    if cs=='1':
        cs10=1
        cs50=0
        cs100=0
        cs500=0
        cs1000=0
        cs5000=0
        cs10000=0
        csg10000=0
    elif cs=='2':
        cs10=0
        cs50=1
        cs100=0
        cs500=0
        cs1000=0
        cs5000=0
        cs10000=0
        csg10000=0
    elif cs=='3':
        cs10=0
        cs50=0
        cs100=1
        cs500=0
        cs1000=0
        cs5000=0
        cs10000=0
        csg10000=0
    elif cs=='4':
        cs10=0
        cs50=0
        cs100=0
        cs500=1
        cs1000=0
        cs5000=0
        cs10000=0
        csg10000=0
    elif cs=='5':
        cs10=0
        cs50=0
        cs100=0
        cs500=0
        cs1000=1
        cs5000=0
        cs10000=0
        csg10000=0
    elif cs=='6':
        cs10=0
        cs50=0
        cs100=0
        cs500=0
        cs1000=0
        cs5000=1
        cs10000=0
        csg10000=0
    elif cs=='7':
        cs10=0
        cs50=0
        cs100=0
        cs500=0
        cs1000=0
        cs5000=0
        cs10000=1
        csg10000=0
    elif cs=='8':
        cs10=0
        cs50=0
        cs100=0
        cs500=0
        cs1000=0
        cs5000=0
        cs10000=0
        csg10000=1

    ct= request.form.get('comtype')
    ctpv=0
    ctes=0
    ctps=0
    ctfs=0
    ctngo=0
    cto=0
    if ct=='1':
        ctpv=1
        ctes=0
        ctps=0
        ctfs=0
        ctngo=0
        cto=0
        
    elif ct=='2':
        ctpv=0
        ctes=1
        ctps=0
        ctfs=0
        ctngo=0
        cto=0
    elif ct=='3':
        ctpv=0
        ctes=0
        ctps=1
        ctfs=0
        ctngo=0
        cto=0
    elif ct=='4':
        ctpv=0
        ctes=0
        ctps=0
        ctfs=1
        ctngo=0
        cto=0
    elif ct=='5':
        ctpv=0
        ctes=0
        ctps=0
        ctfs=0
        ctngo=1
        cto=0
    elif ct=='6':
        ctpv=0
        ctes=0
        ctps=0
        ctfs=0
        ctngo=0
        cto=1       
    lastnew = request.form.get('lastnew')
    training = request.form.get('training')
    citydev=float(citydev)
    r=int(r)
    exp=int(exp)
    lastnew=int(lastnew)
    training=int(training)
    l=[citydev,gm,gu,gf,go,r,en,ef,eu,ep,edg,edm,edhs,0,edphd,edpr,mds,mdb,0,mda,mdh,mdn,mdo,exp,0,cs100,cs10,csg10000,cs10000,cs5000,cs50,cs500,cs1000,0,ctpv,ctfs,ctes,cto,ctps,ctngo,lastnew,training]

    final_features = [np.array(l)]
    prediction = model.predict(final_features)

    output = prediction[0]
    o="def"
    if output==1.0:
        o='Yes'
    else:
        o='No'
    l1=[g,r,e,md,ed,cs,ct]
    print(l)
    print(l1)
    return render_template('index.html', prediction_text='Job change:  {}'.format(o))

if __name__ == "__main__":
    app.run(debug=True)