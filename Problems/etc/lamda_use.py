# lamda �Ű����� : ���ϰ�
# map = �Լ�, list ��Ҹ� �Լ��� �ְ� ��ȯ�� ������ ���ο� ����Ʈ ����
# filter = �Լ�, list ��Ҹ� �Լ��� �ְ� ��ȯ�� ���� True�� ��쿡�� ���ο� ����Ʈ ����

# ����(1)
power = lambda x:x*x
under_3 = lambda x:x<3

list_input_a = [1,2,3,4,5]
output_a = map(power, list_input_a)
output_b = filter(under_3, list_input_a)

print(type(output_a)) # class map
print(type(output_b)) # class filter

print(list(output_a))
print(list(output_b))
