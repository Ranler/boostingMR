-- import UDFs
REGISTER boostingPig.jar;
DEFINE DataGenerator boostingPig.datasets.DataGeneratorLoadFunc;

training = LOAD '$input' USING DataGenerator($wekaparam);

STORE training INTO '$output';
