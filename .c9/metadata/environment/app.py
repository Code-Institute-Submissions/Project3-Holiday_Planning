{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":73,"column":0},"end":{"row":76,"column":41},"action":"insert","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({'_id': ObjectId(task_id)})","    return redirect(url_for('get_tasks'))"],"id":1}],[{"start":{"row":69,"column":0},"end":{"row":71,"column":41},"action":"remove","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    return redirect(url_for('get_tasks'))"],"id":2}],[{"start":{"row":69,"column":0},"end":{"row":70,"column":0},"action":"remove","lines":["",""],"id":3},{"start":{"row":68,"column":42},"end":{"row":69,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":822.6666870117188,"scrollleft":0,"selection":{"start":{"row":68,"column":42},"end":{"row":68,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572622233039,"hash":"6e42b4661edf655ba177c89e77eefb8063a2c962"}