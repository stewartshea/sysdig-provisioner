podTemplate(
label: 'terraform',
cloud: 'openshift',
containers: [
    containerTemplate(name: 'terraform',
                    image: 'hashicorp/terraform',
                    resourceLimitMemory: '512Mi',
                    workingDir:'/home/jenkins'
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