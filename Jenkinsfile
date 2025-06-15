pipeline {
       agent any

       triggers {
       cron("H/2 * * * *")
       }

       parameters {
       string(name: "MESSAGE", defaultValue: "Hello world!", description: "Message to be displayed")
       }

       stages {
           stage("say message") {
                steps {
                echo "Message: ${params.MESSAGE}"
                }
            }
       }
     }