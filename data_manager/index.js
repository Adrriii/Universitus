'use strict';

const db = require('../db');

var sha256=function a(b){function c(a,b){return a>>>b|a<<32-b}for(var d,e,f=Math.pow,g=f(2,32),h="length",i="",j=[],k=8*b[h],l=a.h=a.h||[],m=a.k=a.k||[],n=m[h],o={},p=2;64>n;p++)if(!o[p]){for(d=0;313>d;d+=p)o[d]=p;l[n]=f(p,.5)*g|0,m[n++]=f(p,1/3)*g|0}for(b+="\x80";b[h]%64-56;)b+="\x00";for(d=0;d<b[h];d++){if(e=b.charCodeAt(d),e>>8)return;j[d>>2]|=e<<(3-d)%4*8}for(j[j[h]]=k/g|0,j[j[h]]=k,e=0;e<j[h];){var q=j.slice(e,e+=16),r=l;for(l=l.slice(0,8),d=0;64>d;d++){var s=q[d-15],t=q[d-2],u=l[0],v=l[4],w=l[7]+(c(v,6)^c(v,11)^c(v,25))+(v&l[5]^~v&l[6])+m[d]+(q[d]=16>d?q[d]:q[d-16]+(c(s,7)^c(s,18)^s>>>3)+q[d-7]+(c(t,17)^c(t,19)^t>>>10)|0),x=(c(u,2)^c(u,13)^c(u,22))+(u&l[1]^u&l[2]^l[1]&l[2]);l=[w+x|0].concat(l),l[4]=l[4]+w|0}for(d=0;8>d;d++)l[d]=l[d]+r[d]|0}for(d=0;8>d;d++)for(e=3;e+1;e--){var y=l[d]>>8*e&255;i+=(16>y?0:"")+y.toString(16)}return i};

module.exports = class data_manager {

    constructor() {
        this.db = new db();
    }

    isActive() {
        return this.db.isActive();
    }

    //// NOTICE : Datamanager functions return a promise, not the actual data
    //// To use the data from a function, do as in this example :
    /*
    *
    *   data_manager.getUser(1).then(rows => { // code } );
    * 
    */

    // Get all users from the user table
    getUsers() {
        return this.db.query("SELECT * FROM user");
    }

    // Get one specific user
    getUser(id) {
        return this.db.query("SELECT * FROM user WHERE id = ?", [id]);
    }

    // Get one specific user
    getUserFromUsername(username) {
        return this.db.query("SELECT * FROM user WHERE login LIKE ?", [username]);
    }

    // Sequential, encodes a password
    encodePassword(string) {
        var salt = "fjiz'_ç\"5'9";
        return sha256(string+salt);
    }

    // Create a new user
    registerUser(username, password) {
        return this.db.query("INSERT INTO user (login, pass) VALUES (?,?)", [username,this.encodePassword(password)]);
    }

    // Challenge a password
    checkUserLogin(username, password) {
        return this.db.query("SELECT * FROM user WHERE login = ? AND pass = ?", [username,this.encodePassword(password)]);
    }

    
}