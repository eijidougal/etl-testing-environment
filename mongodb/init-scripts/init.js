db = db.getSiblingDB('testdb');
db.createCollection('users');
db.users.insert({name: 'Test User'});
