podTemplate(
label: 'terraform',
cloud: 'openshift',
containers: [
    containerTemplate(name: 'terraform',
                    image: 'hashicorp/terraform',
                    resourceLimitMemory: '512Mi',
                    workingDir:'/home/jenkins',
                    command: 'sleep infinity'
                    )
    ]
    )
{

    node('terraform') {
    container('terraform')
    {
        stage('Test agent') {
                sh 'echo HELLO WORLD'
        
        }
    }
    }
}