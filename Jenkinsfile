podTemplate(
label: 'tf-applier',
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

    node('tf-applier') {
    container('terraform')
    {
        stage('Test agent') {
                sh 'echo HELLO WORLD'
        
        }
    }
    }
}