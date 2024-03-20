class Response:
  """
    Response Model for clean Formatting
  """
  def __init__(self, status: str, message: str, data: any):
    self.status = status
    self.message = message
    self.data = data
  