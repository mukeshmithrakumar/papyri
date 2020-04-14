var AWS = require('aws-sdk');
var s3 = new AWS.S3();

exports.handler = function (event, context) {
    var s3 = new AWS.S3();
    var param = {
        Bucket: 'papyrisummarytext',
        Key: event.title + '.json',
        Body: JSON.stringify(event)
    };

    s3.upload(param, function (err, data) {
        if (err) console.log(err, err.stack);
        else console.log("Upload Successful");
        context.done();
    });
};
