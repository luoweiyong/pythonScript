# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import CCCommonMessage_pb2 as CCCommonMessage__pb2
import CustomerAnalysisService_pb2 as CustomerAnalysisService__pb2


class CustomerAnalysisServiceStub(object):
  """///////////////////////////////response//////////////////////////////////////
  客户中心客户分析服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.countCustomer = channel.unary_unary(
        '/customercenter.CustomerAnalysisService/countCustomer',
        request_serializer=CustomerAnalysisService__pb2.RequestCountCustomer.SerializeToString,
        response_deserializer=CCCommonMessage__pb2.ReplyMsg.FromString,
        )
    self.countEachMonthCustomer = channel.unary_unary(
        '/customercenter.CustomerAnalysisService/countEachMonthCustomer',
        request_serializer=CustomerAnalysisService__pb2.RequestCountEachMonthCustomer.SerializeToString,
        response_deserializer=CCCommonMessage__pb2.ReplyMsg.FromString,
        )


class CustomerAnalysisServiceServicer(object):
  """///////////////////////////////response//////////////////////////////////////
  客户中心客户分析服务
  """

  def countCustomer(self, request, context):
    """统计客户数(实时统计本月数据)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def countEachMonthCustomer(self, request, context):
    """根据年份统计每月的客户数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerAnalysisServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'countCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.countCustomer,
          request_deserializer=CustomerAnalysisService__pb2.RequestCountCustomer.FromString,
          response_serializer=CCCommonMessage__pb2.ReplyMsg.SerializeToString,
      ),
      'countEachMonthCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.countEachMonthCustomer,
          request_deserializer=CustomerAnalysisService__pb2.RequestCountEachMonthCustomer.FromString,
          response_serializer=CCCommonMessage__pb2.ReplyMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'customercenter.CustomerAnalysisService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))