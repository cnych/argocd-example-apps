#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart

from imports import k8s


class MyChart(Chart):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # 定义标签
        label = {"app": "guestbook-ui"}
        # 定义 Service 对象
        k8s.Service(self, 'service',
                    spec=k8s.ServiceSpec(
                        type='NodePort',
                        ports=[k8s.ServicePort(port=80, target_port=k8s.IntOrString.from_number(80))],
                        selector=label)
                    )
        # 定义 Deployment 对象
        k8s.Deployment(self, 'deployment',
                       spec=k8s.DeploymentSpec(
                         replicas=2,
                         selector=k8s.LabelSelector(match_labels=label),
                         template=k8s.PodTemplateSpec(
                           metadata=k8s.ObjectMeta(labels=label),
                           spec=k8s.PodSpec(containers=[
                             k8s.Container(
                               name='guestbook-ui',
                               image='cnych/ks-guestbook-demo:0.2',
                               ports=[k8s.ContainerPort(container_port=80)])]))))


app = App()
MyChart(app, "cdk8s-guestbook")

app.synth()  # 该方法负责生成生成k8s资源清单文件
