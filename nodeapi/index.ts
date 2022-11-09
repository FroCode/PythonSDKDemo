let {PythonShell} = require('python-shell')

PythonShell.run('../sdk_client.py', null, function (err) {
  if (err) throw err;
  console.log('Command executed sucessfully');
});

