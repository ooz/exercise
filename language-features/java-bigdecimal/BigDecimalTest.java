import java.math.BigDecimal;

/**
 * 0.1 cannot exactly be represented as double floating point
 */
public class BigDecimalTest {
    public static void main(String[] args) {

        BigDecimal fromDouble = new BigDecimal(0.1);
        BigDecimal fromString = new BigDecimal("0.1");
        BigDecimal fromValueOfDouble = BigDecimal.valueOf(0.1);
        Double doubleFromString = new Double("0.1");
        Double doubleFromDouble = new Double(0.1);

        System.out.println(fromDouble);
        System.out.println(fromString);
        System.out.println(fromValueOfDouble);

        System.out.println(doubleFromString);
        System.out.println(doubleFromDouble.doubleValue());

        assert fromValueOfDouble.compareTo(fromDouble) != 0;
        assert fromValueOfDouble.compareTo(fromString) == 0;
        assert doubleFromString.doubleValue() == doubleFromDouble.doubleValue();
    }

}
