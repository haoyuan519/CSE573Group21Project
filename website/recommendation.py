from flask import Blueprint
import pandas as pd
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('recommendation', __name__)


@auth.route('/movie')
def check():
    return render_template("Knnmovie.html")


@auth.route('/movie2')
def check2():
    return render_template("svdmovie.html")


@auth.route('/result', methods=['POST', 'GET'])
def searchmovie():
    # movies_id = request.form['movieId']
    return render_template("movie.html")


@auth.route('/resultSvd', methods=['POST', 'GET'])
def resultSvd():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    print(name)
    df = pd.read_csv("svd.csv")
    var = df.loc[df['movieId'] == int(name)]
    ##var['recommendation'].values.tolist()
    recommendation = var['recommendation'].values.tolist()
    print(recommendation)
    ##var['recommendation'].to_string(index=False)
    recommendations = recommendation[0].replace('[', '').replace(']', '').replace('"', "'")
    # value = re.split('; |, ’|, “', recommendations)
    # print(value[1])
    # for i in range(10):
    #     print(recommendations.split(", '")[i].replace("'", ''))

    return render_template('test2.html', current_movie=var['title'].to_string(index=False),
                           sample_input=recommendations.split(", '")[0].replace("'", ''),
                           sample_input2=recommendations.split(", '")[1].replace("'", ''),
                           sample_input3=recommendations.split(", '")[2].replace("'", ''),
                           sample_input4=recommendations.split(", '")[3].replace("'", ''),
                           sample_input5=recommendations.split(", '")[4].replace("'", ''),
                           sample_input6=recommendations.split(", '")[5].replace("'", ''),
                           sample_input7=recommendations.split(", '")[6].replace("'", ''),
                           sample_input8=recommendations.split(", '")[7].replace("'", ''),
                           sample_input9=recommendations.split(", '")[8].replace("'", ''),
                           sample_input10=recommendations.split(", '")[9].replace("'", ''), )


@auth.route('/resultKnn', methods=['POST', 'GET'])
def resultKnn():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    print(name)
    df = pd.read_csv("Knn.csv")
    var = df.loc[df['movieId'] == int(name)]
    ##var['recommendation'].values.tolist()
    recommendation = var['recommendation'].values.tolist()
    print(recommendation)
    ##var['recommendation'].to_string(index=False)
    recommendations = recommendation[0].replace('[', '').replace(']', '').replace('"', "'")
    # value = re.split('; |, ’|, “', recommendations)
    # print(value[1])
    # for i in range(10):
    #     print(recommendations.split(", '")[i].replace("'", ''))

    return render_template('test3.html', current_movie=var['title'].to_string(index=False),
                           sample_input=recommendations.split(", '")[0].replace("'", ''),
                           sample_input2=recommendations.split(", '")[1].replace("'", ''),
                           sample_input3=recommendations.split(", '")[2].replace("'", ''),
                           sample_input4=recommendations.split(", '")[3].replace("'", ''),
                           sample_input5=recommendations.split(", '")[4].replace("'", ''),
                           sample_input6=recommendations.split(", '")[5].replace("'", ''),
                           sample_input7=recommendations.split(", '")[6].replace("'", ''),
                           sample_input8=recommendations.split(", '")[7].replace("'", ''),
                           sample_input9=recommendations.split(", '")[8].replace("'", ''),
                           sample_input10=recommendations.split(", '")[9].replace("'", ''), )
